var loginSection = document.getElementById("login-section");
var registroSection = document.getElementById("registro-section");
var btnEnviar = document.getElementById('Ingresar');
btnEnviar.addEventListener('click', iniciarSesion);
url_base= "http://18.119.105.122/"
function toggleRegistration() {
  if (loginSection.style.display === "none") {
    loginSection.style.display = "block";
    registroSection.style.display = "none";
  } else {
    loginSection.style.display = "none";
    registroSection.style.display = "block";
  }
}


async function iniciarSesion() {
  var user = document.getElementById('username').value;
  var pass = document.getElementById('password').value;
  const url = url_base+'api/personas/getAll/';
  params = { email: user, password: pass };
  console.log(JSON.stringify(params));

  const response = await fetch(url_base+'api/personas/getAll/', {
    method: 'POST',
    body: JSON.stringify(params),
    headers: {
      'Content-Type': 'application/json'
    }
  });

  const data = await response.text();
  document.open();
  document.write(data);
  document.close();
}

