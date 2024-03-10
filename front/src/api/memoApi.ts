/** @format */

import axios from "axios";

// APIのベースURLをメモのリストを取得するエンドポイントに変更
const BASE_URL = "http://localhost:8000/list/";

export const getMemos = async () => {
  const response = await axios.get(BASE_URL);
  console.log(response.data);
  return response.data;
};

export const createMemo = async (title: string, memo: string) => {
  // POSTリクエストのURLを調整
  const response = await axios.post("http://localhost:8000/create/", {
    title,
    memo,
  });
  return response.data;
};

export const updateMemo = async (id: number, title: string, memo: string) => {
  // PUTリクエストのURLを調整
  const response = await axios.put(`http://localhost:8000/update/${id}/`, {
    title,
    memo,
  });
  return response.data;
};

export const deleteMemo = async (id: number) => {
  // DELETEリクエストのURLを調整
  await axios.delete(`http://localhost:8000/delete/${id}/`);
};
