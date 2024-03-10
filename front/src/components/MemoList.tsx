/** @format */

// frontend/src/components/MemoList.tsx
import React, {useEffect, useState} from "react";
import {getMemos, createMemo, updateMemo, deleteMemo} from "../api/memoApi";

interface Memo {
  id: number;
  title: string;
  memo: string;
}

const MemoList: React.FC = () => {
  const [memos, setMemos] = useState<Memo[]>([]);
  const [title, setTitle] = useState("");
  const [memo, setMemo] = useState("");
  const [selectedMemo, setSelectedMemo] = useState<Memo | null>(null);

  useEffect(() => {
    fetchMemos();
  }, []);

  const fetchMemos = async () => {
    const data = await getMemos();
    setMemos(data);
  };

  const handleCreateMemo = async (e: React.FormEvent) => {
    e.preventDefault();
    const newMemo = await createMemo(title, memo);
    setMemos([...memos, newMemo]);
    setTitle("");
    setMemo("");
  };

  const handleUpdateMemo = async (e: React.FormEvent) => {
    e.preventDefault();
    if (selectedMemo) {
      const updatedMemo = await updateMemo(selectedMemo.id, title, memo);
      const updatedMemos = memos.map((memo) =>
        memo.id === selectedMemo.id ? updatedMemo : memo
      );
      setMemos(updatedMemos);
      setSelectedMemo(null);
      setTitle("");
      setMemo("");
    }
  };

  const handleDeleteMemo = async (id: number) => {
    await deleteMemo(id);
    const updatedMemos = memos.filter((memo) => memo.id !== id);
    setMemos(updatedMemos);
  };

  return (
    <div>
      <h2>Memo List</h2>
      <ul>
        {memos.map((memo) => (
          <li key={memo.id}>
            <h3>{memo.title}</h3>
            <p>{memo.memo}</p>
            <button onClick={() => setSelectedMemo(memo)}>Edit</button>
            <button onClick={() => handleDeleteMemo(memo.id)}>Delete</button>
          </li>
        ))}
      </ul>

      <h2>Create Memo</h2>
      <form onSubmit={handleCreateMemo}>
        <input
          type="text"
          placeholder="Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <textarea
          placeholder="Memo"
          value={memo}
          onChange={(e) => setMemo(e.target.value)}
        ></textarea>
        <button type="submit">Create</button>
      </form>

      {selectedMemo && (
        <div>
          <h2>Update Memo</h2>
          <form onSubmit={handleUpdateMemo}>
            <input
              type="text"
              placeholder="Title"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
            />
            <textarea
              placeholder="Memo"
              value={memo}
              onChange={(e) => setMemo(e.target.value)}
            ></textarea>
            <button type="submit">Update</button>
          </form>
        </div>
      )}
    </div>
  );
};

export default MemoList;
