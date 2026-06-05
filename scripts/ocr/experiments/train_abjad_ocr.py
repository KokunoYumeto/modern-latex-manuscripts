#!/usr/bin/env python3
"""Train a CNN to read printed abjad numerals 0-360 from table cells.
Formulation: 3 digit-heads (hundreds/tens/units, 10 classes each) — matches abjad structure,
far easier than 361-way. Synthetic data in Naskh fonts (AmiriQuran dropped: renders tofu) with
print-like degradation. Saves abjad_cnn.pt. Real-print transfer validated separately. GPU."""
import numpy as np, random, torch, torch.nn as nn
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import arabic_reshaper
from bidi.algorithm import get_display
random.seed(0); np.random.seed(0); torch.manual_seed(0)

FONTS=[r'C:\Windows\Fonts\Amiri-Regular.ttf', r'C:\Windows\Fonts\Amiri-Bold.ttf',
       r'C:\Windows\Fonts\NotoNaskhArabic-Regular.ttf', r'C:\Windows\Fonts\NotoNaskhArabic-Bold.ttf',
       r'C:\Windows\Fonts\Scheherazade-Regular.ttf', r'C:\Windows\Fonts\Scheherazade-Bold.ttf']
U=['','ا','ب','ج','د','ه','و','ز','ح','ط']; T=['','ي','ك','ل','م','ن','س','ع','ف','ص']
Hd=['','ق','ر','ش','ت','ث','خ','ذ','ض','ظ']
def abj(n): return Hd[n//100]+T[(n%100)//10]+U[n%10]
W,H=96,64; _fc={}
def font(p,s):
    if (p,s) not in _fc: _fc[(p,s)]=ImageFont.truetype(p,s)
    return _fc[(p,s)]
def render(n):
    s=get_display(arabic_reshaper.reshape(abj(n)))
    f=font(random.choice(FONTS), random.randint(34,50))
    img=Image.new('L',(W,H),255); d=ImageDraw.Draw(img)
    bb=d.textbbox((0,0),s,font=f); tw,th=bb[2]-bb[0],bb[3]-bb[1]
    d.text(((W-tw)//2-bb[0]+random.randint(-4,4),(H-th)//2-bb[1]+random.randint(-4,4)),s,font=f,fill=random.randint(0,45))
    if random.random()<0.6: img=img.filter(ImageFilter.GaussianBlur(random.uniform(0.3,1.1)))
    a=np.array(img,dtype=np.float32)+np.random.normal(0,random.uniform(0,20),(H,W))
    if random.random()<0.3: a=np.where(a<random.randint(100,160),0.,255.)
    return np.clip(a,0,255)/255.0
def batch(n):
    ns=np.random.randint(0,361,n)
    X=torch.tensor(np.stack([render(int(v)) for v in ns])[:,None],dtype=torch.float32)
    H3=torch.tensor([(v//100, (v%100)//10, v%10) for v in ns],dtype=torch.long)
    return X, H3, ns
class Net(nn.Module):
    def __init__(s):
        super().__init__()
        s.b=nn.Sequential(nn.Conv2d(1,32,3,1,1),nn.ReLU(),nn.MaxPool2d(2),
            nn.Conv2d(32,64,3,1,1),nn.ReLU(),nn.MaxPool2d(2),
            nn.Conv2d(64,128,3,1,1),nn.ReLU(),nn.AdaptiveAvgPool2d(4),nn.Flatten(),
            nn.Linear(128*16,256),nn.ReLU(),nn.Dropout(0.3))
        s.h=nn.Linear(256,10); s.t=nn.Linear(256,10); s.u=nn.Linear(256,10)
    def forward(s,x):
        z=s.b(x); return s.h(z),s.t(z),s.u(z)
dev='cuda'; net=Net().to(dev); opt=torch.optim.Adam(net.parameters(),1e-3); lf=nn.CrossEntropyLoss()
Xv,Yv,nv=batch(3000); Xv,Yv=Xv.to(dev),Yv.to(dev)
print('[train] start (3-digit-head)',flush=True)
for ep in range(12):
    net.train(); Xt,Yt,_=batch(18000); Xt,Yt=Xt.to(dev),Yt.to(dev)
    for i in range(0,18000,256):
        opt.zero_grad(); ph,pt,pu=net(Xt[i:i+256])
        (lf(ph,Yt[i:i+256,0])+lf(pt,Yt[i:i+256,1])+lf(pu,Yt[i:i+256,2])).backward(); opt.step()
    net.eval()
    with torch.no_grad():
        ph,pt,pu=net(Xv); val=100*ph.argmax(1)+10*pt.argmax(1)+pu.argmax(1)
        acc=(val.cpu().numpy()==nv).mean()
    print(f'epoch {ep:2d} synthetic_val_acc {acc:.3f}',flush=True)
torch.save(net.state_dict(), r'albattani_work\rebuilt\abjad_cnn.pt')
print('[train] saved abjad_cnn.pt',flush=True)
