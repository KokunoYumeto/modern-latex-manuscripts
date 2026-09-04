"""Arrange already-rendered final PDF pages for bounded visual inspection."""
import importlib.util, math
from pathlib import Path
from PIL import Image,ImageDraw
path=Path(__file__).with_name('build_d019_integration.py')
spec=importlib.util.spec_from_file_location('builder',path);b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
for lang in ('EN','FR'):
    files=sorted(p for p in (b.AUDIT/'visual').glob(lang+'-D019-*.png') if p.stem.rsplit('-',1)[-1].isdigit())
    canvas=Image.new('RGB',(1100,800*math.ceil(len(files)/2)),(225,229,234));draw=ImageDraw.Draw(canvas)
    for i,p in enumerate(files):
        image=Image.open(p).convert('RGB');image.thumbnail((520,760))
        x=(i%2)*550+(550-image.width)//2;y=(i//2)*800+28
        canvas.paste(image,(x,y));draw.text((x,y-19),p.name,fill='black')
    canvas.save(b.AUDIT/'visual'/f'{lang}-D019-contact.png')
files=[b.AUDIT/'visual'/f'{lang}-{work}-boundary.png' for lang in ('EN','FR') for work in ('D018','D021')]
canvas=Image.new('RGB',(1100,1600),(225,229,234));draw=ImageDraw.Draw(canvas)
for i,p in enumerate(files):
    image=Image.open(p).convert('RGB');image.thumbnail((520,760));x=(i%2)*550+(550-image.width)//2;y=(i//2)*800+28
    canvas.paste(image,(x,y));draw.text((x,y-19),p.name,fill='black')
canvas.save(b.AUDIT/'visual/INSERTION_BOUNDARIES_contact.png')
