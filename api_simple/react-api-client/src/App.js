import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
    const [message, setMessage] = useState('');

    useEffect(() => {
        axios.get('http://localhost:3001/api/greet')
            .then(response => {
                setMessage(response.data.message);
            })
            .catch(error => {
                console.error('Error fetching the API:', error);
            });
    }, []);

    return (
        <div className="App">
            <h1>{message}</h1>
        </div>
    );
}

export default App;
