//this would be the object shape for storing the questions  
 //you can change the questions to your own taste or even add more questions..
 const questions = [
    {
        question: "HCF of 8, 9, 25 is",
        optionA: "8",
        optionB: "9",
        optionC: "25",
        optionD: "1",
        correctOption: "optionD"
    },

    {
        question: "Which of the following is not irrational?",
        optionA: "(2 – √3)2",
        optionB: "(√2 + √3)2",
        optionC: "√2 -√3)(√2 + √3)",
        optionD: "2√7/7",
        correctOption: "optionC"
    },

    {
        question: "If the zeroes of the quadratic polynomial x^2 + (a + 1) x + b are 2 and -3, then",
        optionA: "a = -7, b = -1",
        optionB: "a = 5, b = -1",
        optionC: "a = 2, b = -6",
        optionD: "a = 0, b = -6",
        correctOption: "optionD"
    },

    {
        question: "The number of polynomials having zeroes as 2 and 5 is",
        optionA: "1",
        optionB: "2",
        optionC: "3",
        optionD: "More than 3",
        correctOption: "optionD"
    },

    {
        question: "The pair of equations 3x + 5y = 7 and + 6x + 10y = 7 have",
        optionA: "a unique solution",
        optionB: "infinitely many solutions",
        optionC: "no solution",
        optionD: "two solutions",
        correctOption: "optionC"
    },

    {
        question: "If a pair of linear equations is consistent, then the lines will be",
        optionA: "always coincident",
        optionB: "parallel",
        optionC: "always intersecting",
        optionD: "intersecting or coincident",
        correctOption: "optionD"
    },

    {
        question: "The quadratic equation has degree",
        optionA: "0",
        optionB: "1",
        optionC: "2",
        optionD: "3",
        correctOption: "optionC"
    },

    {
        question: "Which of the following is not a quadratic equation",
        optionA: "x^2 + 3x + 5 = 0",
        optionB: "x^2 + x^3 + 2 = 0",
        optionC: "3 + x + x^2 = 0",
        optionD: "x^2 + 9 = 0",
        correctOption: "optionB"
    },

    {
        question: "Which of these numbers is an odd number ?",
        optionA: "Ten",
        optionB: "Twelve",
        optionC: "Eight",
        optionD: "Eleven",
        correctOption: "optionD"
    },

    {
        question: "If p, q, r and s are in A.P. then r minus q is",
        optionA: "s - p",
        optionB: "s - q",
        optionC: "s - r",
        optionD: "none of the above",
        correctOption: "optionC"
    },

    {
        question: "If the sum of three numbers in an A.P. is 9 and their product is 24, then numbers are",
        optionA: "2,4,6",
        optionB: "1,5,3",
        optionC: "2,8,4",
        optionD: "2,3,4",
        correctOption: "optionD"
    },

    {
        question: "The probability of getting a spade card from a well shuffled deck of 52 cards is ?",
        optionA: "1/13",
        optionB: "1/4",
        optionC: "12/13",
        optionD: "3/4",
        correctOption: "optionB"
    },


    {
        question: "The probability of getting exactly one head in tossing a pair of coins is ?",
        optionA: "0",
        optionB: "1/2",
        optionC: "1",
        optionD: "1/3",
        correctOption: "optionB"
    },

    
    {
        question: "How many sides does an hexagon have ?",
        optionA: "Six",
        optionB: "Sevene",
        optionC: "Four",
        optionD: "Five",
        correctOption: "optionA"
    },

    
]


let shuffledQuestions = [] //empty array to hold shuffled selected questions out of all available questions

function handleQuestions() { 
    //function to shuffle and push 10 questions to shuffledQuestions array
//app would be dealing with 10questions per session
    while (shuffledQuestions.length <= 9) {
        const random = questions[Math.floor(Math.random() * questions.length)]
        if (!shuffledQuestions.includes(random)) {
            shuffledQuestions.push(random)
        }
    }
}


let questionNumber = 1 //holds the current question number
let playerScore = 0  //holds the player score
let wrongAttempt = 0 //amount of wrong answers picked by player
let indexNumber = 0 //will be used in displaying next question

// function for displaying next question in the array to dom
//also handles displaying players and quiz information to dom
function NextQuestion(index) {
    handleQuestions()
    const currentQuestion = shuffledQuestions[index]
    document.getElementById("question-number").innerHTML = questionNumber
    document.getElementById("player-score").innerHTML = playerScore
    document.getElementById("display-question").innerHTML = currentQuestion.question;
    document.getElementById("option-one-label").innerHTML = currentQuestion.optionA;
    document.getElementById("option-two-label").innerHTML = currentQuestion.optionB;
    document.getElementById("option-three-label").innerHTML = currentQuestion.optionC;
    document.getElementById("option-four-label").innerHTML = currentQuestion.optionD;

}


function checkForAnswer() {
    const currentQuestion = shuffledQuestions[indexNumber] //gets current Question 
    const currentQuestionAnswer = currentQuestion.correctOption //gets current Question's answer
    const options = document.getElementsByName("option"); //gets all elements in dom with name of 'option' (in this the radio inputs)
    let correctOption = null

    options.forEach((option) => {
        if (option.value === currentQuestionAnswer) {
            //get's correct's radio input with correct answer
            correctOption = option.labels[0].id
        }
    })

    //checking to make sure a radio input has been checked or an option being chosen
    if (options[0].checked === false && options[1].checked === false && options[2].checked === false && options[3].checked == false) {
        document.getElementById('option-modal').style.display = "flex"
    }

    //checking if checked radio button is same as answer
    options.forEach((option) => {
        if (option.checked === true && option.value === currentQuestionAnswer) {
            document.getElementById(correctOption).style.backgroundColor = "green"
            playerScore++ //adding to player's score
            indexNumber++ //adding 1 to index so has to display next question..
            //set to delay question number till when next question loads
            setTimeout(() => {
                questionNumber++
            }, 1000)
        }

        else if (option.checked && option.value !== currentQuestionAnswer) {
            const wrongLabelId = option.labels[0].id
            document.getElementById(wrongLabelId).style.backgroundColor = "red"
            document.getElementById(correctOption).style.backgroundColor = "green"
            wrongAttempt++ //adds 1 to wrong attempts 
            indexNumber++
            //set to delay question number till when next question loads
            setTimeout(() => {
                questionNumber++
            }, 1000)
        }
    })
}



//called when the next button is called
function handleNextQuestion() {
    checkForAnswer() //check if player picked right or wrong option
    unCheckRadioButtons()
    //delays next question displaying for a second just for some effects so questions don't rush in on player
    setTimeout(() => {
        if (indexNumber <= 9) {
//displays next question as long as index number isn't greater than 9, remember index number starts from 0, so index 9 is question 10
            NextQuestion(indexNumber)
        }
        else {
            handleEndGame()//ends game if index number greater than 9 meaning we're already at the 10th question
        }
        resetOptionBackground()
    }, 1000);
}

//sets options background back to null after display the right/wrong colors
function resetOptionBackground() {
    const options = document.getElementsByName("option");
    options.forEach((option) => {
        document.getElementById(option.labels[0].id).style.backgroundColor = ""
    })
}

// unchecking all radio buttons for next question(can be done with map or foreach loop also)
function unCheckRadioButtons() {
    const options = document.getElementsByName("option");
    for (let i = 0; i < options.length; i++) {
        options[i].checked = false;
    }
}

// function for when all questions being answered
function handleEndGame() {
    let remark = null
    let remarkColor = null

    // condition check for player remark and remark color
    if (playerScore <= 3) {
        remark = "Bad Grades, Keep Practicing."
        remarkColor = "red"
    }
    else if (playerScore >= 4 && playerScore < 7) {
        remark = "Average Grades, You can do better."
        remarkColor = "orange"
    }
    else if (playerScore >= 7) {
        remark = "Excellent, Keep the good work going."
        remarkColor = "green"
    }
    const playerGrade = (playerScore / 10) * 100

    //data to display to score board
    document.getElementById('remarks').innerHTML = remark
    document.getElementById('remarks').style.color = remarkColor
    document.getElementById('grade-percentage').innerHTML = playerGrade
    document.getElementById('wrong-answers').innerHTML = wrongAttempt
    document.getElementById('right-answers').innerHTML = playerScore
    document.getElementById('score-modal').style.display = "flex"

}

//closes score modal, resets game and reshuffles questions
function closeScoreModal() {
    questionNumber = 1
    playerScore = 0
    wrongAttempt = 0
    indexNumber = 0
    shuffledQuestions = []
    NextQuestion(indexNumber)
    document.getElementById('score-modal').style.display = "none"
}

//function to close warning modal
function closeOptionModal() {
    document.getElementById('option-modal').style.display = "none"
}
