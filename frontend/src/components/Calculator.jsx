import { useEffect, useState } from "react";

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
        <div>

            <h1>Calculator</h1>

            <form onSubmit={handleCalculate}>

                <input
                    type="number"
                    placeholder="First Number"
                    value={num1}
                    onChange={(event) =>
                        setNum1(event.target.value)
                    }
                />

                <br />
                <br />

                <input
                    type="number"
                    placeholder="Second Number"
                    value={num2}
                    onChange={(event) =>
                        setNum2(event.target.value)
                    }
                />

                <br />
                <br />

                <select
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

                <br />
                <br />

                <button type="submit">
                    Calculate
                </button>

            </form>


            <br />

            {result && (

                <div>

                    <h2>
                        Result
                    </h2>

                    <p>
                        {result.result}
                    </p>

                </div>

            )}


            <hr />

            <h2>
                History
            </h2>

            {history.map((item) => (

                <div key={item.id}>

                    <p>

                        {item.num1}

                        {" "}

                        {item.operation}

                        {" "}

                        {item.num2}

                        {" = "}

                        {item.result}

                    </p>

                </div>

            ))}

        </div>
    );
}


export default Calculator;