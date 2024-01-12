import { useEffect } from "react";

function useOutsideAlerter(
  ref: React.RefObject<HTMLDivElement>,
  handleClickOutsideCallback: () => void
) {
  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (ref.current && !ref.current.contains(event.target as Node)) {
        handleClickOutsideCallback();
      }
    }
    document.addEventListener("mousedown", handleClickOutside);
    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, [ref]); 
}

export default useOutsideAlerter;
