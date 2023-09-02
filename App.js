// frontend/src/App.js

import React, { useState } from "react";
import "./App.css";

function App() {
  const [prompt, setPrompt] = useState("");
  const [imageData, setImageData] = useState("");

  const handleInputChange = (e) => {
    setPrompt(e.target.value);
  };

  const handleSubmit = async () => {
    try {
      const response = await fetch("/generate-image/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ prompt }),
      });

      if (!response.ok) {
        throw new Error("Image generation failed");
      }

      const data = await response.json();
      setImageData(data.image_data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="App">
      <h1>Text to Image Generator</h1>
      <div className="input-container">
        <input
          type="text"
          placeholder="Enter a prompt..."
          value={prompt}
          onChange={handleInputChange}
        />
        <button onClick={handleSubmit}>Generate</button>
      </div>
  
      <div className="image-container">
        <img src={`data:image/png;base64,${imageData}`} alt="Generated" />
      </div>
      
    </div>
  );
}

export default App;
