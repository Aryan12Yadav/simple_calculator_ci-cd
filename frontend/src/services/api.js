import axios from "axios"

const api = axios.create({
    baseURL:"http://127.0.0.1:8000"
})

export const calculateResult = async (formData) => {
    const response = await api.post(
        "/calculator/calculate",
        formData,
        {
            headers:{
                "Content-Type":"multipart/form-data"
            }
        }
    );  
    return  response.data
};

export const getHistory = async () => {
    const response = await api.get(
        "/calculator/history"
    );
    return response.data;
};
export default api;