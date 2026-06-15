import axios from "axios"

const api = axios.create({
    // baseURL:"https://calculator-api-7ntd.onrender.com"
    baseURL: import.meta.env.VITE_API_URL
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