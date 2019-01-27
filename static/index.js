fetch('api/vote')
  .then(response => response.json())
  .then(data => {
  	console.log(data)
  	const yes_ = document.getElementById("yes")
  	yes_.innerText = data.yes
  	const no_ = document.getElementById("no")
  	no_.innerText = data.no

  })

 