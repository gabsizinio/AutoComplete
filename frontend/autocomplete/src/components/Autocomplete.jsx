import { useState, useEffect } from "react";
import { useLazyQuery, gql } from "@apollo/client";
import "./Autocomplete.css";

const GET_SUGGESTIONS = gql`
  query GetSuggestions($term: String!) {
    suggestions(term: $term) {
      id
      text
    }
  }
`;

export default function Autocomplete() {
    const [term, setTerm] = useState("");
    const [highlight, setHighlight] = useState("");
    const [suggestionsList, setSuggestionsList] = useState([]);
    const [getSuggestions] = useLazyQuery(GET_SUGGESTIONS);

    useEffect(() => {
        const timer = setTimeout(() => {
            if (term.length >= 4) {
                setSuggestionsList([]);
                setHighlight(term);
                getSuggestions({ variables: { term } }).then((res) => {
                    setSuggestionsList(res.data?.suggestions || []);
                });
            } else {
                setSuggestionsList([]); // limpa sugestões se tiver menos de 4 letras
            }
        }, 1); // debounce de 300ms

        return () => clearTimeout(timer);
    }, [term]);

    const handleClick = (text) => {
        setTerm(text);
        setSuggestionsList([]); // esconde a lista após clique
    };

    const highlightText = (text) => {
        const idx = text.toLowerCase().indexOf(highlight.toLowerCase());
        if (idx === -1) return text;

        return (
            <>
                {text.slice(0, idx)}
                <strong>{text.slice(idx, idx + highlight.length)}</strong>
                {text.slice(idx + highlight.length)}
            </>
        );
    };

    return (
        <div className="autocomplete-container">
            <input
                type="text"
                placeholder="Digite ao menos 4 letras..."
                value={term}
                onChange={(e) => setTerm(e.target.value)}
            />
            {suggestionsList.length > 0 && (
                <ul className="autocomplete-list">
                    {suggestionsList.map((s) => (
                        <li key={s.id} onClick={() => handleClick(s.text)}>
                            {highlightText(s.text)}
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
}

