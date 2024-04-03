var isResolvingCaptcha = false;
function getAnswers(img) {
    fetch('http://127.0.0.1:5000/solve', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ image: img })
    })
        .then(response => {
            if (response.ok) {
                return response.json();
            }
            throw new Error('Network response was not ok.');
        })
        .then(data => {
            console.log('Response from server:', data);
            const answers = data['answer'] || [];
            for (const answer of answers) {
                console.log(answer)
                const randomTimeout = Math.floor(Math.random() * 3000) + 1000
                setTimeout(() => {
                    Engine.captcha.addSelectedAnswer(answer)
                }, randomTimeout)
            }

            // accept the captcha:
            const confirmCaptchaInterval = setInterval(() => {
                const sortedAnswers = answers.slice().sort();
                const sortedSelectedAnswer = Engine.captcha.getSelectedAnswer().slice().sort();
                console.log("current answers: " + JSON.stringify(sortedAnswers) + " selected answers: " + JSON.stringify(sortedSelectedAnswer))
                if (JSON.stringify(sortedAnswers) === JSON.stringify(sortedSelectedAnswer)) {

                    console.log("Confirming captcha...")
                    Engine.captcha.confirmOnClick({ isTrusted: true })
                    clearInterval(confirmCaptchaInterval)
                    isResolvingCaptcha = false;
                }
            }, 1500)
        })

        .catch(error => {
            // Handle errors
            console.error('There was a problem with the fetch operation:', error);
        });

}

function runAntiCaptcha() {
    if (isResolvingCaptcha) return;
    if (!Engine.lock.list.includes('captcha')) return

    const captchaDiv = document.querySelector('.captcha__image')
    const imgElement = captchaDiv.querySelector('img');
    const imgSrc = imgElement.getAttribute('src');

    isResolvingCaptcha = true;
    const answers = getAnswers(imgSrc);
}

const a = setInterval(runAntiCaptcha, 1000);

//code is nasty, but workin tho 