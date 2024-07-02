//this would be the object shape for storing the questions  
 //you can change the questions to your own taste or even add more questions..
 const questions = [
    {
        question: "The change in the direction of a wave passing from one medium to another is termed as ",
        optionA: "Inerference",
        optionB: "Mirage",
        optionC: "Diffraction",
        optionD: "Refraction",
        correctOption: "optionD"
    },

    {
        question: "What would be the angle of incidence for a light ray having zero reflection angle?",
        optionA: "180",
        optionB: "90",
        optionC: "0",
        optionD: "45",
        correctOption: "optionC"
    },

    {
        question: "Twinkling of stars is due to which optical phenomenon?",
        optionA: "Reflection",
        optionB: "Diffraction",
        optionC: "Divergence",
        optionD: "Refraction",
        correctOption: "optionD"
    },

    {
        question: "Light from the Sun falling on a convex lens will converge at",
        optionA: "R",
        optionB: "C",
        optionC: "F",
        optionD: "P",
        correctOption: "optionC"
    },

    {
        question: "Concave lens produces",
        optionA: "virtual image",
        optionB: "erect image",
        optionC: "diminished image",
        optionD: "all of the above",
        correctOption: "optionD"
    },

    {
        question: "A defect in human eye due to which the person can only see nearby objects is known as",
        optionA: "Myopia",
        optionB: "Hypermetropia",
        optionC: "Presbyopia",
        optionD: "Catarct",
        correctOption: "optionA"
    },

    {
        question: "The power of a lens is taken out by which fomula",
        optionA: "1/v + 1/u",
        optionB: "2f",
        optionC: "r/2",
        optionD: "1/f",
        correctOption: "optionD"
    },

    {
        question: "Oxidation is a process which involves",
        optionA: "addition of oxygen",
        optionB: "exchange of ions",
        optionC: "reduction of oxygen",
        optionD: "addition of hydrogen",
        correctOption: "optionA"
    },

    {
        question: "Give the ratio in which hydrogen and oxygen are present in water by volume.",
        optionA: "1:2",
        optionB: "2:1",
        optionC: "3:2",
        optionD: "2:3",
        correctOption: "optionB"
    },

    {
        question: "Identify the substance oxidized in this equation. MnO2 + 4HCl → 2 + 2H2O + Cl2",
        optionA: "MnCl2",
        optionB: "HCl",
        optionC: "MnO2",
        optionD: "H2O",
        correctOption: "optionC"
    },

    {
        question: "A substance X is used in white-washing and is obtained by heating limestone in the absence of air. Identify X.",
        optionA: "Quick Lime",
        optionB: "Slaked Lime",
        optionC: "Calcium Carbonate",
        optionD: "Sodium bicarbonate",
        correctOption: "optionA"
    },

    {
        question: "Which of the following are energy foods?",
        optionA: "Proteins and mineral salts",
        optionB: "Carbohydrates and fats",
        optionC: "Vitamins and minerals",
        optionD: "Water and roughage",
        correctOption: "optionB"
    },


    {
        question: "The mode of nutrition found in fungi is:",
        optionA: "Parasitic nutrition",
        optionB: "Holozoic nutrition",
        optionC: "Autotrophic nutrition",
        optionD: "Saprotrophic nutrition",
        correctOption: "optionD"
    },

    
    {
        question: "Roots of the plants absorb water from the soil through the process of:",
        optionA: "diffusion",
        optionB: "transpiration",
        optionC: "osmosis",
        optionD: "None of these",
        correctOption: "optionC"
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