import axios from "axios";

export default axios.create({
  baseURL: 'http://34.64.197.76/api',
  headers: {
    "Content-type": "application/json"
  }
});