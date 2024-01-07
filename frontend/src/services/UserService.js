import axios from './customize-axios';

const fetchAllHotel = () => {
    return axios.get('http://127.0.0.1:8000/hotel/all');
}

export { fetchAllHotel } 