import Listagem from "./components/listagem";
import Link from 'next/link'

export default function Home() {
  return (
    <div className="p-4">
      
        <Link className="bg-blue-600 text-white p-2 rounded hover:bg-blue-800"
        href="/incluir">Cadastrar</Link>

        <Listagem />
        
    </div>
  );
}
