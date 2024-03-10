/** @format */

import axios from "axios";

const BASE_URL = "http://localhost:8000/";

export const getMemos = async () => {
  const response = await axios.get(BASE_URL);
  return response.data;
};

export const createMemo = async (title: string, memo: string) => {
  const response = await axios.post(BASE_URL, {title, memo});
  return response.data;
};

export const updateMemo = async (id: number, title: string, memo: string) => {
  const response = await axios.put(`${BASE_URL}${id}/`, {title, memo});
  return response.data;
};

export const deleteMemo = async (id: number) => {
  await axios.delete(`${BASE_URL}${id}/`);
};
