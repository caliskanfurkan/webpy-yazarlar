import web

urls = (
	'/', 'AnaSayfa',
	'/DetayGor/(\d+)', 'DetayGoster'
)

db = web.database(dbn='mysql', user='yazarlar', pw='6857874', db='yazarlar') 
render = web.template.render('templates/')


class AnaSayfa:
	def GET(self):
		yazilar = db.select('yazilar')
		return render.index(yazilar)

class DetayGoster:
	def GET(self, id):
		id = int(id)
		detay = db.select('yazilar', where='id=$id',vars=locals())[0]
		return render.detail(detay)


if __name__ == "__main__":
	app = web.application(urls, globals())
	app.internalerror = web.debugerror
	app.run()
