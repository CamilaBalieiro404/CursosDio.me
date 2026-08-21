var a = 'a' //dificilmente utilizada 
let b = 'b'
const c = 'c'

let d :string = 'd'
let n: number = 1
let x: boolean = true

let m: string | number = '1'
m = 'Camila'
m = 31



b = '2'
d = '3'


const pessoa = {
    nome: 'Camila',
    idade: 31,
    profissao: 'Desenvolvedora'
}

//Boas praticas de tipagem

interface Pessoa {
    nome: string,
    idade: number,
    profissao?: string//? um tipo Opcional, ou seja, pode ou não ser definido
}//? string | underfined

const pessoa2: Pessoa = {
    nome: 'Camila',
    idade: 31,
    profissao: 'Desenvolvedora'
}

const pessoa3: Pessoa = {
    nome: 'João',
    idade: 25
}

//Boas praticas de tipagem

const pessoa4: {nome: string, idade: number, profissao?: string} = {
    nome: 'Camila',
    idade: 31,
    profissao: 'Desenvolvedora'
}

const pessoa7 : Array<string> = ['Camila', 'João', 'Maria']

const arrayDePessoas: Array<Pessoa> = [
    {
        nome: 'Camila', 
        idade: 31,
        profissao: 'Desenvolvedora'
    },
]

const arraynumero: Array<number> = [1, 2, 3, 4, 5]

const arraystring : Array<string> = ['Camila', 'João', 'Maria']

const arrayboolean : Array<boolean> = [true, false, true]
