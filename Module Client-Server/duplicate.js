function findDuplicates(){
    const numbers = [2,4,5,2,5,8,5,10];
    for(let i=0;i<numbers.length;i++){
        const numberAtI = numbers[i];
        for(let j=0; j<numbers.length;j++)
        {
            const numberAtJ = numbers[j];
            if(numberAtI === numberAtJ){
                console.log(`Doppelte Zahl gefunden:${numberAtI}`);
            }
        }
    }
}

findDuplicates()


function findDuplicatesRight(){
    const numbers = [2,4,5,2,5,8,5,10];
    for(let i=0;i<numbers.length;i++){
        var numberAtI = numbers[i];
        for(let j=i+1; j<numbers.length;j++)
        {
            var numberAtJ = numbers[j];
            if(numberAtI === numberAtJ){
                console.log(`Doppelte Zahl gefunden:${numberAtI}`);
            }
        }
    }
}

findDuplicatesRight()