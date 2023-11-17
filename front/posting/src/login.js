// src/LoginPage.js
import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import './login.scss';

function LoginPage() {
    const [user_id, setUserId] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();
    const url = 'http://127.0.0.1:8000' 

    const moveToSignUp = () => {
        navigate('/SignUp');
    }

    const moveToFindPw = () => { 
        navigate('/FindPw');
    }

    const handleSubmitClick = (e) => {
        const endpoint = '/api/auth/login';
        const payload = {
            email: user_id,  // Using the studentNumber state
            password: password
        };

        // navigate('/PostitTable');
        e.preventDefault();

        axios.post(url + endpoint, payload)
            .then(response => {
                console.log(response);
                localStorage.setItem('sex', response.data.sex);
                localStorage.setItem('token', response.data.access_token);
                localStorage.setItem('refresh_token', response.data.refresh_token);
                navigate('/PostitTable');
            })
            .catch(error => {
                console.error("Error fetching data:", error);
            });
    };

    return (
      <div>
        {/* <h2>Login</h2> */}
        <form className="login" onSubmit={handleSubmitClick}>
            <h2>Login</h2>
          <div>
            <label>
              <input
                type="text"
                placeholder="Username"
                value={user_id}
                onChange={(e) => setUserId(e.target.value)}
              />
            </label>
          </div>
          <br/>
          <div>
            <label>
              <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </label>
          </div>
          <br/>
          <button type="submit" onClick={handleSubmitClick} style={{marginRight: 5}}>Login</button>
          <button onClick={moveToSignUp} style={{marginLeft: 5, marginRight: 5}}>SignUp</button>
          <button onClick={moveToFindPw} style={{marginLeft: 5}}>Find PW</button>
        </form>
      </div>
    );
}

export default LoginPage;
