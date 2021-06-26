import request from '../utils/request';

export const gethotlist = () => {
    return request({
        url: 'http://localhost:7000/api/v1/hotlist',
        method: 'get',
    });
}
