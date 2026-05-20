import { useState } from "react";
import axios from "axios";

function App() {

  const [message, setMessage] = useState("");
  const [response, setResponse] = useState(null);

  const sendMessage = async () => {

    try {

      const res = await axios.post(
        "http://127.0.0.1:8000/chat",
        {
          message: message
        }
      );

      setResponse(res.data);

    } catch (error) {

      console.error(error);

    }
  };

  return (
  <div
  style={{
    display: "flex",
    width: "100vw",
    minHeight: "100vh",
    fontFamily: "Arial",
    backgroundColor: "#f4f7fb",
    margin: 0,
    padding: 0
  }}
>

    {/* LEFT PANEL */}

    <div
      style={{
        width: "50%",
        padding: "40px",
        borderRight: "1px solid #ddd",
        backgroundColor: "white"
      }}
    >

      <h1>MediRoute AI</h1>

      <p>
        AI-Powered Healthcare Workflow Orchestration
      </p>

      <textarea
        rows="10"
        placeholder="Describe your healthcare request..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        style={{
          width: "100%",
          padding: "15px",
          marginTop: "20px",
          fontSize: "16px",
          borderRadius: "10px",
          border: "1px solid #ccc"
        }}
      />

      <button
        onClick={sendMessage}
        style={{
          marginTop: "20px",
          padding: "14px 28px",
          backgroundColor: "#2563eb",
          color: "white",
          border: "none",
          borderRadius: "10px",
          cursor: "pointer",
          fontSize: "16px"
        }}
      >
        Analyze Request
      </button>

    </div>

    {/* RIGHT PANEL */}

    <div
      style={{
        width: "50%",
        padding: "40px"
      }}
    >

      <h2>AI Workflow Analysis</h2>

      {!response && (
        <p>
          Submit a healthcare request to view AI workflow analysis.
        </p>
      )}

      {response && (

        <div
          style={{
            marginTop: "20px",
            backgroundColor: "white",
            padding: "25px",
            borderRadius: "12px",
            boxShadow: "0 2px 10px rgba(0,0,0,0.1)"
          }}
        >

          <p>
            <strong>Status:</strong> {response.status}
          </p>

          <p>
            <strong>Intent:</strong> {response.intent}
          </p>

          <p>
            <strong>Escalation:</strong> {response.escalation}
          </p>

          {response.intent === "appointment" && (

  <div
    style={{
      marginTop: "25px",
      padding: "25px",
      backgroundColor: "#ffffff",
      borderRadius: "12px",
      border: "1px solid #ddd"
    }}
  >

    <h3>Appointment Intake Form</h3>

    {/* Specialty */}

    <div style={{ marginTop: "15px" }}>

      <label>
        Specialty
      </label>

      <br />

      <select
        style={{
          width: "100%",
          padding: "10px",
          marginTop: "8px",
          borderRadius: "8px"
        }}
      >
        <option>Cardiology</option>
        <option>Dermatology</option>
        <option>Neurology</option>
        <option>Pediatrics</option>
        <option>Orthopedics</option>
      </select>

    </div>

    {/* Time Slots */}

    <div style={{ marginTop: "20px" }}>

      <label>
        Available Time Slots
      </label>

      <br />

      <select
        style={{
          width: "100%",
          padding: "10px",
          marginTop: "8px",
          borderRadius: "8px"
        }}
      >
        <option>Tomorrow - 10:00 AM</option>
        <option>Tomorrow - 2:30 PM</option>
        <option>Friday - 11:00 AM</option>
        <option>Friday - 4:00 PM</option>
      </select>

    </div>

    {/* Appointment Type */}

    <div style={{ marginTop: "20px" }}>

      <label>
        Appointment Type
      </label>

      <br />

      <div style={{ marginTop: "10px" }}>

        <input type="radio" name="appointmentType" />
        {" "}Virtual

        <br />

        <input type="radio" name="appointmentType" />
        {" "}In-Person

      </div>

    </div>

    {/* Phone Number */}

    <div style={{ marginTop: "20px" }}>

      <label>
        Phone Number
      </label>

      <br />

      <input
        type="text"
        placeholder="Enter phone number"
        style={{
          width: "100%",
          padding: "10px",
          marginTop: "8px",
          borderRadius: "8px",
          border: "1px solid #ccc"
        }}
      />

    </div>

    {/* Insurance */}

    <div style={{ marginTop: "20px" }}>

      <label>
        Insurance Provider
      </label>

      <br />

      <input
        type="text"
        placeholder="Enter insurance provider"
        style={{
          width: "100%",
          padding: "10px",
          marginTop: "8px",
          borderRadius: "8px",
          border: "1px solid #ccc"
        }}
      />

    </div>

    {/* Button */}

    <button
      style={{
        marginTop: "25px",
        padding: "12px 24px",
        backgroundColor: "#16a34a",
        color: "white",
        border: "none",
        borderRadius: "10px",
        cursor: "pointer",
        fontSize: "16px"
      }}
    >
      Schedule Appointment
    </button>

  </div>

)}

          {response.no_show_prediction && (
            <div
              style={{
                marginTop: "20px",
                padding: "20px",
                backgroundColor: "#fef3c7",
                borderRadius: "10px"
              }}
            >

              <h3>No-Show Prediction</h3>

              <p>
                <strong>Risk Level:</strong>
                {" "}
                {response.no_show_prediction.risk_level}
              </p>

              <p>
                <strong>Reason:</strong>
                {" "}
                {response.no_show_prediction.reason}
              </p>

              <p>
                <strong>Recommended Action:</strong>
                {" "}
                {response.no_show_prediction.recommended_action}
              </p>

            </div>
          )}

        </div>

      )}

    </div>

  </div>
);
}
export default App;