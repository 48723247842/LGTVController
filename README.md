# LG TV Controller

### Based on https://github.com/TheRealLink/pylgtv

```
x = LGTVController({
	"ip_address": "192.168.1.99" ,
	"port": 3000 ,
	"mac_address": "AA:BB:CC:DD:EE:FF" ,
	"client_key": "12346789abcdefghijklmnopqrstuvwx" ,
	"always_wakeup": True
})
pprint( x.get_current_app() )
pprint( x.power_off() )
```