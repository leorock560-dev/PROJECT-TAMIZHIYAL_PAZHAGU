let GrammarInput=document.querySelector(".input");
let Subject=document.getElementById("subject");
let Object_=document.getElementById("object");
let Verb=document.getElementById("verb");
let Tense=document.getElementById("tense");
let TransInput=document.getElementById("trans_input");
const GrammarCorrector=document.getElementById("grammar");
const SentenceBuilder=document.getElementById("sentence-builder");
const Transliterator=document.getElementById("transliterator");
const GrammarFeature=document.querySelector(".grammar-corrector-feature");
const SentenceBuilderFeature=document.querySelector(".sentence-builder-feature");
const TransliteratorFeature=document.querySelector(".transliterator-feature");

GrammarInput.addEventListener("input",()=>{

document.getElementById("count").innerText=
GrammarInput.value.length+" / 500 characters";

});

function clearGrammer(){

GrammarInput.value="";
document.getElementById("count").innerText="0 / 500 characters";

}

function clearSentence(){

Subject.value="";
Object_.value="";
Verb.value="";
Tense.value="";

}
function clearTransliteration(){

TransInput.value="";
document.getElementById("trans_count").innerText="0 / 500 characters";

}

function copyOutput(){

navigator.clipboard.writeText(
document.getElementById("output").innerText
);

alert("Copied!");

}

function showPage1(page) {

    GrammarCorrector.style.display = "none";
    SentenceBuilder.style.display = "none";
    Transliterator.style.display = "none";

    page.style.display = "flex";
}

function showGram(page) {

    GrammarCorrector.style.display = "flex";
    SentenceBuilder.style.display = "none";
    Transliterator.style.display = "none";
}


function showTrans(page) {

    GrammarCorrector.style.display = "none";
    SentenceBuilder.style.display = "none";
    Transliterator.style.display = "flex";
}


function showSent(page) {

    GrammarCorrector.style.display = "none";
    SentenceBuilder.style.display = "flex";
    Transliterator.style.display = "none";
}


document.querySelector(".grammar_corrector")
.addEventListener("click", () => {
    showPage1(GrammarCorrector);
});

document.querySelector(".sentence_builder")
.addEventListener("click", () => {
    showPage1(SentenceBuilder);
});

document.querySelector(".transliteration")
.addEventListener("click", () => {
    showPage1(Transliterator);
});

function clearText(btn){

    let card = btn.closest(".card");

    let input = card.querySelector("textarea,input");

    input.value = "";

}
async function correctSentence() {

    let text = document.getElementById("grammar_input").value;

    let response = await fetch("http://127.0.0.1:5000/grammar_corrector", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            text: text
        })
    });

    let data = await response.json();
    console.log(data);

    document.getElementById("output").innerText = data.output;
    document.getElementById("error_type").innerText = data.error_type;
    document.getElementById("explanation").innerText = data.explanation;
}
async function transliterate() {

    let text = document.getElementById("trans_input").value;

    let response = await fetch("http://127.0.0.1:5000/transliterator", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            text: text
        })
    });

    let data = await response.json();
    console.log(data);

    document.getElementById("trans_output").innerText = data.output;
}
async function sentenceBuilder() {

    let subject = document.getElementById("subject").value;
    let object = document.getElementById("object").value;
    let verb = document.getElementById("verb").value;
    let tense = document.getElementById("tense").value;

    let response = await fetch("http://127.0.0.1:5000/sentence_builder", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            subject: subject,
            object: object,
            verb: verb,
            tense: tense
        })
    });

    let data = await response.json();
    console.log(data);

    document.getElementById("sent_output").innerText = data.output;
}
function logOut(){

    window.location.href = "login_index.html";
}