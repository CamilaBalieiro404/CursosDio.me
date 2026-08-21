const num: number = 10;

if(num > 15){
    console.log('Maior que 15')
}else{
    console.log('Menor que 15')
}

const typeUser = {
    admin:'Seja bem vindo admin',
    student:'Voce é um estudante',
    viewer:'Voce pode visualizar o conteudo'
}

function validarUser(user: string){
    console.log(typeUser[user as keyof typeof typeUser])
}

const usuario = "admin"
validarUser(usuario)
validarUser("student")
validarUser("viewer")