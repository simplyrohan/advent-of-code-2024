from pygame import*
from random import*
t=display
d=t.set_mode()
m=Vector2
s=m(),
v=1,0
f=m(v)
while not event.get(256):
 h=s[-1];d.fill(0);k=key.get_pressed()
 if 1 in k:v=k[K_d]-k[97],k[K_s]-k[K_w]
 for b in*s,f:draw.circle(d,-1,b*9,4)
 s+=h+v,;t.flip();time.wait(99)
 if h==f:f.xy=choices(range(99),k=2)
 else:_,*s=s