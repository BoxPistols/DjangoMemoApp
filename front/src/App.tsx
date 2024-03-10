/** @format */

// frontend/src/App.tsx
import React from "react";
import MemoList from "./components/MemoList";

const App: React.FC = () => {
  return (
    <div>
      <h1>Memo App</h1>
      <MemoList />
    </div>
  );
};

export default App;
