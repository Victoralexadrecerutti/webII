export default function Listagem() {
  return (
    <div className="m-8 text-center">
      <h1 className="text-2xl">Pessoas</h1>

      <table className="table-fixed border m-auto">
        <thead>
          <tr>
            <th>Música</th>
            <th>Artista</th>
            <th>Ano</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>The Sliding Mr. Bones (Next Stop, Pottersville)</td>
            <td>Malcolm Lockyer</td>
            <td>1961</td>
          </tr>
          <tr>
            <td>Witchy Woman</td>
            <td>The Eagles</td>
            <td>1972</td>
          </tr>
          <tr>
            <td>Shining Star</td>
            <td>Earth, Wind, and Fire</td>
            <td>1975</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}
