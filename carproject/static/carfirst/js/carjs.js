var tl = gsap.timeline();


tl 
  .from(".animate",{
  x:890,
  duration:1
  })
  .from(".brand",{
    y:100,
    duration:1
  })
  .to(".animate",{
    x:-1300,
    duration:2,
    
  })
  .to(".topscreen",{
    top:"-103%",
    
    duration:1.2,
    ease:"power4.easeOut"

  })
  .from(".navEmerge",{
    y:10,
    opacity:0,
    duration:2
  })
  .to(",navEmerge",{
    y:0,
    duration:1
  })
  .from(".place",{
    opacity:0,
    duration:2,
	delay:-.5
  })
 
