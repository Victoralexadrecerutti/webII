import FormPessoa from "../components/form_pessoa";
import Link from 'next/link'

export default function Incluir() {
  return (
    <div className="p-4">
        <Link 
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700" 
        href="/">Início</Link>
        <main className="text-center text-2xl">
        Nova Pessoa
        </main>
        <FormPessoa />
    </div>
  );
}
