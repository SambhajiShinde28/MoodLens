import React, { useRef, useState } from "react";
import './MoodLensHomePageDesign.css'
import axios from "axios";

const MoodLensHomePage = () => {

    const reviewTextRef = useRef()
    const [modelResponse, setModelResponse] = useState("None")

    const AnalyseBTNClicked = async () => {

        setModelResponse("None")

        if (reviewTextRef.current.value !== "") {

            const response = await axios.post("http://127.0.0.1:8000/predict", { review: reviewTextRef.current.value });

            if (response.data.sentiment === "Positive") {
                setModelResponse("😊 Yay! That's a positive vibe!");
            }
            else {
                setModelResponse("😔 Oh no! That sounds negative.");
            }
        }
        else {
            alert("Please, Insert Text !!")
        }
    }


    return (

        <div className="main-container">

            <header>
                <h1>MoodLink</h1>
            </header>

            <div className="container">
                <div className="subcontainer">
                    <h2>Analyse Sentiment</h2>
                    <input type="text" ref={reviewTextRef} placeholder="Enter your text" />
                    <button type="button" onClick={AnalyseBTNClicked}>Analyse</button>
                    <h3>Response</h3>
                    <p id="responceTest">{modelResponse}</p>
                </div>
            </div>

        </div>

    )
}

export default MoodLensHomePage