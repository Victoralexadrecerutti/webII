export default function FormPessoa() {
  return (
    <div>
      <form className="flex flex-col">
        
        <label>Nome: </label>
        <input className="border" type="text" name="nome" />
        
        <label>Email: </label>
        <input className="border" type="text" name="email" />
        
        <label>Telefone: </label>
        <input className="border" type="text" name="telefone" />
        
        <button className="border mt-4" type="submit">Incluir!</button>
        
      </form>
    </div>
  );
}
