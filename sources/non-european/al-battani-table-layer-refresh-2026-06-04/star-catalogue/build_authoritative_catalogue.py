#!/usr/bin/env python3
"""Build the COMPLETE al-Battani fixed-star catalogue from authoritative coordinates.

Coordinate source: C. A. Nallino, *Al-Battani sive Albatenii Opus Astronomicum*,
Pars II (1907), the printed Latin table "Situs et magnitudines stellarum fixarum
anno 1191 a Dhu 'l-qarnayn" (epoch ~880 CE). Read directly from the Toronto/IA scan
of the combined 1899-1907 edition. Longitudes are ABSOLUTE ecliptic degrees; plaga
b=borealis(N)/a=australis(S); magnitude is al-Battani's rank. Modern Bayer/Flamsteed
IDs are Nallino's marginal identifications. Bright-star latitudes were cross-checked
against modern ecliptic values (Sirius -39.6, Vega +61.7, Arcturus +30.7, etc.).

The Escorial codex is missing a leaf (Argo Navis incl. Canopus + Hydra + start of
Crater); Nallino documents this lacuna and it is recorded here, not silently skipped.

Arabic + Chinese descriptions are merged from the project's trilingual reading
(star_catalogue.csv) where they align by constellation; remaining Arabic is pending.
Data file: nallino_cat.tsv (single source of truth for coordinates).
"""
import csv, os, subprocess
HERE=os.path.dirname(os.path.abspath(__file__))
GRIND=os.path.join(os.path.dirname(os.path.dirname(HERE)),'grind')  # ...\WINDOWS 32\grind
TSV=os.path.join(GRIND,'nallino_cat.tsv')

# ---- constellation metadata: catalogue order, Latin, Arabic (translit + script), Chinese ----
CONST_META=[
 ('UrsaMinor','Ursa Minor','ad-dubb al-asghar','الدب الأصغر','小熊座'),
 ('UrsaMajor','Ursa Major','ad-dubb al-akbar','الدب الأكبر','大熊座'),
 ('Draco','Draco','at-tinnin','التنين','天龙座'),
 ('Cephaeus','Cepheus','qifawus / al-multahib','قيفاوس','仙王座'),
 ('Bootes','Bootes','al-baqqar / al-'+'awwa','العواء','牧夫座'),
 ('CoronaBorealis','Corona Borealis','al-fakkah','الفكة','北冕座'),
 ('Hercules','Hercules','al-jathi','الجاثي','武仙座'),
 ('Lyra','Lyra','an-nasr al-waqi','النسر الواقع','天琴座'),
 ('Cygnus','Cygnus','ad-dajajah','الدجاجة','天鹅座'),
 ('Cassiopeia','Cassiopeia','dhat al-kursi','ذات الكرسي','仙后座'),
 ('Perseus','Perseus','hamil ra'+'s al-ghul / barshawush','حامل رأس الغول','英仙座'),
 ('Auriga','Auriga','mumsik al-a'+'innah','ممسك الأعنة','御夫座'),
 ('Ophiuchus','Ophiuchus','al-hawwa','الحواء','蛇夫座'),
 ('Serpens','Serpens','al-hayyah','الحية','巨蛇座'),
 ('Sagitta','Sagitta','as-sahm','السهم','天箭座'),
 ('Aquila','Aquila','an-nasr at-ta'+'ir','النسر الطائر','天鹰座'),
 ('Delphinus','Delphinus','ad-dulfin','الدلفين','海豚座'),
 ('Equuleus','Equuleus','qit'+'at al-faras','قطعة الفرس','小马座'),
 ('Pegasus','Pegasus','al-faras al-a'+'zam','الفرس الأعظم','飞马座'),
 ('Andromeda','Andromeda','al-mar'+'ah al-musalsalah','المرأة المسلسلة','仙女座'),
 ('Triangulum','Triangulum','al-muthallath','المثلث','三角座'),
 ('Aries','Aries','al-hamal','الحمل','白羊座'),
 ('Taurus','Taurus','ath-thawr','الثور','金牛座'),
 ('Gemini','Gemini','al-jawza'+' / at-taw'+'aman','الجوزاء','双子座'),
 ('Cancer','Cancer','as-saratan','السرطان','巨蟹座'),
 ('Leo','Leo','al-asad','الأسد','狮子座'),
 ('Virgo','Virgo','as-sunbulah / al-'+'adhra','السنبلة','室女座'),
 ('Libra','Libra','al-mizan','الميزان','天秤座'),
 ('Scorpius','Scorpius','al-'+'aqrab','العقرب','天蝎座'),
 ('Sagittarius','Sagittarius','al-qaws / ar-rami','القوس','人马座'),
 ('Capricornus','Capricornus','al-jady','الجدي','摩羯座'),
 ('Aquarius','Aquarius','ad-dalw / sakib al-ma','الدلو','宝瓶座'),
 ('Pisces','Pisces','as-samakatan / al-hut','السمكتان','双鱼座'),
 ('Cetus','Cetus','qitus / sabu'+' al-bahr','قيطس','鲸鱼座'),
 ('Orion','Orion','al-jabbar / al-jawza','الجبار','猎户座'),
 ('Eridanus','Eridanus','an-nahr','النهر','波江座'),
 ('Lepus','Lepus','al-arnab','الأرنب','天兔座'),
 ('CanisMajor','Canis Major','al-kalb al-akbar','الكلب الأكبر','大犬座'),
 ('CanisMinor','Canis Minor','al-kalb al-asghar','الكلب الأصغر','小犬座'),
 ('LACUNA',None,None,None,None),
 ('Crater','Crater','al-ka'+'s / al-baturiyah','الكأس','巨爵座'),
 ('Corvus','Corvus','al-ghurab','الغراب','乌鸦座'),
 ('Centaurus','Centaurus','qantawris / az-zulman','قنطورس','半人马座'),
 ('Lupus','Lupus','as-sabu','السبع','豺狼座'),
 ('Ara','Ara','al-mijmarah','المجمرة','天坛座'),
 ('CoronaAustralis','Corona Australis','al-iklil al-janubi','الإكليل الجنوبي','南冕座'),
 ('PiscisAustralis','Piscis Austrinus','al-hut al-janubi','الحوت الجنوبي','南鱼座'),
]
META={k:(lat,artr,arsc,zh) for k,lat,artr,arsc,zh in CONST_META}
ORDER=[k for k,*_ in CONST_META]

COMMON={ # tidy common names for display
 'Polaris':'Polaris','Kochab':'Kochab','Pherkad':'Pherkad','Dubhe':'Dubhe','Merak':'Merak',
 'Megrez':'Megrez','Phecda':'Phecda','Alioth':'Alioth','Mizar':'Mizar','Alkaid':'Alkaid',
 'Thuban':'Thuban','Arcturus':'Arcturus','Alphecca':'Alphecca','Rasalgethi':'Rasalgethi',
 'Vega':'Vega','Sheliak':'Sheliak','Sulafat':'Sulafat','Albireo':'Albireo','Sadr':'Sadr',
 'Deneb':'Deneb','Schedar':'Schedar','Caph':'Caph','Mirfak':'Mirfak','Algol':'Algol',
 'Capella':'Capella','Menkalinan':'Menkalinan','Rasalhague':'Rasalhague','Tarazed':'Tarazed',
 'Altair':'Altair','Alpheratz':'Alpheratz','Algenib':'Algenib','Scheat':'Scheat','Markab':'Markab',
 'Enif':'Enif','Mirach':'Mirach','Almach':'Almach','Mesarthim':'Mesarthim','Sheratan':'Sheratan',
 'Hamal':'Hamal','Aldebaran':'Aldebaran','ElNath':'Elnath','Pleiades':'Pleiades','Hyades':'Hyades',
 'Castor':'Castor','Pollux':'Pollux','Praesepe':'Praesepe (M44)','AsellusBor':'Asellus Borealis',
 'AsellusAus':'Asellus Australis','Acubens':'Acubens','Regulus':'Regulus','Algieba':'Algieba',
 'Adhafera':'Adhafera','Zosma':'Zosma','Denebola':'Denebola','Porrima':'Porrima',
 'Vindemiatrix':'Vindemiatrix','Spica':'Spica','Zubenelgenubi':'Zubenelgenubi',
 'Zubeneschamali':'Zubeneschamali','Antares':'Antares','Shaula':'Shaula','DenebAlgedi':'Deneb Algedi',
 'Sadalmelik':'Sadalmelik','Sadalsuud':'Sadalsuud','Fomalhaut':'Fomalhaut','Alrescha':'Alrescha',
 'Menkar':'Menkar','Diphda':'Diphda','Betelgeuse':'Betelgeuse','Bellatrix':'Bellatrix',
 'Mintaka':'Mintaka','Alnilam':'Alnilam','Alnitak':'Alnitak','Rigel':'Rigel','Saiph':'Saiph',
 'Acamar':'Acamar','Arneb':'Arneb','Nihal':'Nihal','Sirius':'Sirius','Phact-alphaColumbae':'Phact',
 'betaColumbae':'β Columbae','Gomeisa':'Gomeisa','Procyon':'Procyon','Hadar':'Hadar',
 'RigilKentaurus':'Rigil Kentaurus',
}
GREEK={'alpha':'α','beta':'β','gamma':'γ','delta':'δ','epsilon':'ε','zeta':'ζ','eta':'η','theta':'θ',
 'iota':'ι','kappa':'κ','lambda':'λ','mu':'μ','nu':'ν','xi':'ξ','omicron':'ο','pi':'π','rho':'ρ',
 'sigma':'σ','tau':'τ','upsilon':'υ','phi':'φ','chi':'χ','psi':'ψ','omega':'ω'}
def fmt_bayer(b):
    if not b or b=='-': return ''
    base=b.rstrip('0123456789'); sup=b[len(base):]
    g=GREEK.get(base)
    if g: return g+(sup if sup else '')
    return b  # Flamsteed / letter designations as-is

def load_backbone():
    NB={}
    for r in csv.reader(open(TSV,encoding='utf-8'),delimiter='\t'):
        if not r or r[0].startswith('#'): continue
        const=r[0]
        rec=dict(n=r[1],lod=r[2],lom=r[3],lad=r[4],lam=r[5],plaga=r[6],mag=r[7],
                 bayer=(r[8] if len(r)>8 else ''),note=(r[9] if len(r)>9 else ''))
        NB.setdefault(const,[]).append(rec)
    return NB

def load_arabic():
    """My trilingual reading -> arabic desc per (display constellation)."""
    rows=list(csv.DictReader(open(os.path.join(HERE,'star_catalogue.csv'),encoding='utf-8')))
    by={}
    for r in rows: by.setdefault(r['constellation'],[]).append(r)
    return by

# constellations where my reading count == Nallino count -> safe index merge
def main():
    NB=load_backbone(); AR=load_arabic()
    # reverse map display->nallino key
    disp2key={META[k][0]:k for k in META if META[k][0]}
    # build merged records
    out=[]
    for const in ORDER:
        if const=='LACUNA':
            out.append(dict(const='LACUNA')); continue
        lat,artr,arsc,zh=META[const]
        recs=NB.get(const,[])
        # find my arabic list for this constellation (match by display name)
        mine=AR.get(lat,[])
        use_index = (len(mine)==len(recs) and len(mine)>0)
        # also name-anchor by common name
        for i,rec in enumerate(recs):
            ar_desc=''
            if use_index: ar_desc=mine[i]['arabic']
            out.append(dict(const=const,const_lat=lat,const_ar=arsc,const_artr=artr,const_zh=zh,
                n=rec['n'],bayer=fmt_bayer(rec['bayer']),
                common=COMMON.get(rec['note'],'') or (COMMON.get(rec['bayer'],'')),
                lon_d=rec['lod'],lon_m=rec['lom'],lat_d=rec['lad'],lat_m=rec['lam'],
                dir=('N' if rec['plaga']=='b' else ('S' if rec['plaga']=='a' else '')),
                mag=rec['mag'],arabic=ar_desc,note=rec['note']))
    # write authoritative CSV
    cols=['const','const_lat','const_ar','const_artr','const_zh','n','bayer','common',
          'lon_d','lon_m','lat_d','lat_m','dir','mag','arabic','note']
    pcsv=os.path.join(HERE,'albattani_catalogue_authoritative.csv')
    with open(pcsv,'w',newline='',encoding='utf-8') as fh:
        w=csv.DictWriter(fh,fieldnames=cols); w.writeheader()
        for r in out:
            if r.get('const')=='LACUNA':
                w.writerow({'const':'LACUNA','note':'missing leaf: Argo Navis (Canopus), Hydra, start of Crater'}); continue
            w.writerow(r)
    nstars=sum(1 for r in out if r.get('const')!='LACUNA')
    print(f'authoritative CSV: {nstars} stars -> {os.path.basename(pcsv)}')
    return out,nstars

if __name__=='__main__': main()
