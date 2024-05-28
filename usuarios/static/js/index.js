const form = document.getElementById('form');
const nome = document.getElementById('nome');
const campos = document.querySelectorAll('.inputs')
const email = document.getElementById('email');
const senha = document.getElementById('senha');
const confirmarSenha = document.getElementById("confirmar-senha");
const radioEstudante = document.getElementById('estudante')
const radioInstrutor = document.getElementById('instrutor')
const labelMensagemErro = document.querySelectorAll('.mensagem--erro')
const formBtn = document.getElementById('botao-cadastro')
const spinner = document.querySelector('.spinner')

const msgError = document.getElementById("msgError");

form.addEventListener('submit', function (e) {
        e.preventDefault(); // Prevent the default form submission


        if (validar()) {
          form.submit()
         
        }
        });
        
        
        function validar() {
          let mensagem;
          let isValid = true;
          
          spinner.classList.add("outer-ring");
          
          campos.forEach((campo) => {
    if (campo.value === "") {
      setErrorMessage(campo, `${campo.getAttribute("id")} deve ser preenchido`);
      isValid = false;
    } else {
      removeErrorMessage(campo);
    }
  });
  
  
  if (email.value !== "") {
    const isValidEmail = checkEmail(email.value);
    if (!isValidEmail) {
      mensagem = `${email.getAttribute("id")} não possui o formato correto`;
      setErrorMessage(email, mensagem);

      isValid = false;
    } else {
      removeErrorMessage(email);
    }
  } else {
    setErrorMessage(email, "Email deve ser preenchido");
    isValid = false;
  }


  if (senha.value !== "") {
    const isValidPassword = checkPassword(senha.value);
    if (!isValidPassword) {
      mensagem = `${senha.getAttribute(
        "id"
      )} deve conter pelo menos 1 número e 1 caractere especial`;

      setErrorMessage(senha, mensagem);
      isValid = false;
    } else {
      removeErrorMessage(senha);
    }
  } else {
    setErrorMessage(senha, "Senha deve ser preenchida");
    isValid = false;
  }


  if (confirmarSenha.value !== senha.value) {
    mensagem = `Não coincide com a senha`;
    setErrorMessage(confirmarSenha, mensagem);

    isValid = false;
  } else {
    removeErrorMessage(confirmarSenha);
  }

  // Radio Inputs validation
  if (radioEstudante.checked || radioInstrutor.checked) {
    removeErrorMessage(radioEstudante);
  } else {
    mensagem = "Pelo menos uma das opções deve ser selecionada";
    setErrorMessage(radioEstudante, mensagem);
    isValid = false;
  }

  if (!isValid) {
    spinner.classList.remove("outer-ring");
    return false;
  }



  return true;


}


function checkEmail(email) {
    const regex = new RegExp("^[\\w.-]+@([\\w-]+\\.)+[\\w-]{2,4}$");
    
    const result = regex.test(email);
    return result;
}

function checkPassword(password) {
    const regex = new RegExp(
      "^(?=.*\\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$"
    );
    
    const result = regex.test(password);
    return result;
}


function setErrorMessage(campo, mensagem) {     
    console.log('erro em:', campo.getAttribute('id'))   
    
    spinner.classList.remove("outer-ring");
    campo.style.border = "red";
    campo.style.border = "red 1px solid";
    
    let labelError = campo.nextElementSibling;
    labelError.textContent = mensagem;

    
}

function removeErrorMessage(campo) {
    campo.style.background = "white";
    campo.style.border = "1.55px solid #222";
    
    let labelError = campo.nextElementSibling;
    labelError.textContent = ' '
}


 function getCsrfToken() {
   return document.querySelector("[name=csrfmiddlewaretoken]").value;
 }


