import { useState } from 'react'

export default function Upload() {
  const [result, setResult] = useState(null)

  const handleUpload = async (e) => {
    const file = e.target.files[0]
    const formData = new FormData()
    formData.append('file', file)

    const res = await fetch('/api/verify', {
      method: 'POST',
      body: formData
    })

    const data = await res.json()
    setResult(data)
  }

  return (
    <div>
      <input type="file" onChange={handleUpload} />
      {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
    </div>
  )
}