import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
    const initialState = {
        Pregnancies: '',
        Glucose: '',
        BloodPressure: '',
        SkinThickness: '',
        Insulin: '',
        BMI: '',
        DiabetesPedigreeFunction: '',
        Age: ''
    };

    const [formData, setFormData] = useState(initialState);
    const [result, setResult] = useState('');
    const [isLoading, setIsLoading] = useState(false);

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setIsLoading(true);
        try {
            const response = await axios.post('http://localhost:5000/predict', formData);
            setResult(response.data.result);
        } catch (error) {
            console.error("Error in prediction:", error);
            setResult("Error during prediction.");
        } finally {
            setIsLoading(false);
        }
    };

    const clearAll = (e) => {
        e.preventDefault();
        setFormData(initialState);
        setResult('');
    };

    // Field descriptions for better UX
    const fieldDescriptions = {
        Pregnancies: 'Number of pregnancies',
        Glucose: 'Plasma glucose concentration (mg/dL)',
        BloodPressure: 'Diastolic blood pressure (mm Hg)',
        SkinThickness: 'Triceps skin fold thickness (mm)',
        Insulin: 'Serum insulin (mu U/ml)',
        BMI: 'Body mass index (weight in kg/(height in m)²)',
        DiabetesPedigreeFunction: 'Diabetes pedigree function',
        Age: 'Age in years'
    };

    return (
        <div className="container">
            <h1 className="app-header">Diabetes Risk Assessment</h1>

            <div className="prediction-card">
                <form onSubmit={handleSubmit}>
                    <div className="form-grid">
                        {Object.keys(formData).map((key) => (
                            <div className="form-group" key={key}>
                                <label htmlFor={key} title={fieldDescriptions[key]}>
                                    {key}
                                </label>
                                <input
                                    id={key}
                                    className="form-control"
                                    type="number"
                                    step="any"
                                    name={key}
                                    value={formData[key]}
                                    onChange={handleChange}
                                    placeholder={fieldDescriptions[key]}
                                    required
                                />
                            </div>
                        ))}
                    </div>

                    <div className="btn-container">
                        <button
                            className="btn btn-primary"
                            type="submit"
                            disabled={isLoading}
                        >
                            {isLoading ? 'Processing...' : 'Predict Risk'}
                        </button>
                        <button
                            className="btn btn-secondary"
                            onClick={clearAll}
                        >
                            Clear Form
                        </button>
                    </div>
                </form>
            </div>

            {result && (
                <div className="result-container">
                    <h3>Prediction Result</h3>
                    <p>{result}</p>
                </div>
            )}
        </div>
    );
}

export default App;