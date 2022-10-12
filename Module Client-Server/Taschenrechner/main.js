const resultField = document.querySelector('.trCalculator__result');
const buttonFieldList = document.querySelectorAll('.trCalculator__gridItem');
let input = '';

buttonFieldList.forEach((item) => {
  item.addEventListener('click', (e) => {
    const currentTargetValue = e.currentTarget.innerHTML;
    if (e.currentTarget.classList.contains('trCalculator__gridItem--number') || e.currentTarget.classList.contains('trCalculator__gridItem--operation')) {
      input = input + currentTargetValue;
      resultField.innerHTML = input;
    }
    if (e.currentTarget.classList.contains('trCalculator__gridItem--operationEqual')) {
      let last = input.slice(-1);
      if (input !== '' && last !== '/' && last !== '+' && last !== '-' && last !== 'x') {
        input = eval(input);
        resultField.innerHTML = input;
      }
    }
    if (e.currentTarget.classList.contains('trCalculator__gridItem--actionReset')) {
      input = '';
      resultField.innerHTML = 0;
    }
  });
});
