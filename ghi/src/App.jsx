import { BrowserRouter, Routes, Route } from 'react-router-dom'
import MainPage from "./Home"

function App() {

  return (
    <BrowserRouter>
      <div>
        <Routes>
          <Route path="/" element={<MainPage />} />
        </Routes>
      </div>
    </BrowserRouter>
  )
}

export default App
