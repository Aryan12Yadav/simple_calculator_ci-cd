import { useEffect, useState } from "react";

import "./Calculator.css";

import {
    calculateResult,
    getHistory
} from "../services/api";


function Calculator() {

    const [num1, setNum1] = useState("");
    const [num2, setNum2] = useState("");

    const [operation, setOperation] = useState("add");

    const [result, setResult] = useState(null);

    const [history, setHistory] = useState([]);


    const loadHistory = async () => {

        try {

            const data = await getHistory();

            setHistory(data);

        } catch (error) {

            console.error(error);
        }
    };


    const handleCalculate = async (event) => {

        event.preventDefault();

        try {

            const formData = new FormData();

            formData.append("num1", num1);
            formData.append("num2", num2);
            formData.append("operation", operation);

            const data = await calculateResult(
                formData
            );

            setResult(data);

            loadHistory();

        } catch (error) {

            console.error(error);
        }
    };


    useEffect(() => {

        loadHistory();

    }, []);


    return (

        <div className="container">

            <h1 className="title">
                Calculator
            </h1>

            <form onSubmit={handleCalculate}>

                <input
                    className="input-field"
                    type="number"
                    placeholder="First Number"
                    value={num1}
                    onChange={(event) =>
                        setNum1(event.target.value)
                    }
                    required
                />

                <input
                    className="input-field"
                    type="number"
                    placeholder="Second Number"
                    value={num2}
                    onChange={(event) =>
                        setNum2(event.target.value)
                    }
                    required
                />

                <select
                    className="select-field"
                    value={operation}
                    onChange={(event) =>
                        setOperation(event.target.value)
                    }
                >
                    <option value="add">
                        Add
                    </option>

                    <option value="subtract">
                        Subtract
                    </option>

                    <option value="multiply">
                        Multiply
                    </option>

                    <option value="divide">
                        Divide
                    </option>

                </select>

                <button
                    className="button"
                    type="submit"
                >
                    Calculate
                </button>

            </form>


            {result && (

                <div className="result-box">

                    <h2>
                        Result
                    </h2>

                    <h3>
                        {result.result}
                    </h3>

                </div>

            )}


            <div className="history-box">

                <h2>
                    Calculation History
                </h2>

                {

                    history.length === 0 ? (

                        <p>
                            No calculations found.
                        </p>

                    ) : (

                        history.map((item) => (

                            <div
                                className="history-item"
                                key={item.id}
                            >

                                <p>

                                    {item.num1}

                                    {" "}

                                    {item.operation}

                                    {" "}

                                    {item.num2}

                                    {" = "}

                                    <strong>
                                        {item.result}
                                    </strong>

                                </p>

                            </div>

                        ))

                    )

                }

            </div>

        </div>

    );
}


export default Calculator;