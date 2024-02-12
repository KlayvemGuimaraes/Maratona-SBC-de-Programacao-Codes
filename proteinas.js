var lines = ['10 7','AAACAACTGA','CGGACAA','6','1 1','2 7','5 7',
'6 7',
'4 5',
'6 6' ]
var nums = lines.shift().split(' ') //'10', '7'
var dna = lines.shift()
var proteina = lines.shift()

var consultas = Number(lines.shift())
while(consultas>0){// for(let i = 0; i < consultas; i++){
    var indexes = lines.shift().split(' ')
    let A = Number(indexes[0]) - 1
    let B = Number(indexes[1])

    var subs = proteina.substring(A,B)
    var contagem = 0 

    for(let j = 0; j < (Number(nums[0])); j++){
      if(dna.substring(j, j + subs.length) == subs){
        contagem++
      }     
    }
    console.log(contagem)
    consultas--;
}