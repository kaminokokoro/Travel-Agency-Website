import React from "react";
import { ReactNode } from "react";

export interface Heading2Props {
  heading?: ReactNode;
  subHeading?: ReactNode;
  className?: string;
  name?: string;
  khachsan?: number | string;
}

const Heading2: React.FC<Heading2Props> = ({
  className = "",
  heading = "Hà Nội",
  subHeading,
  khachsan,
}) => {
  return (
    <div className={`mb-12 lg:mb-16 ${className}`}>
      <h2 className="text-4xl font-semibold">{heading}</h2>
      {subHeading ? (
        subHeading
      ) : (
        <span className="block text-neutral-500 dark:text-neutral-400 mt-3">
          Hiện có {khachsan} khách sạn
        </span>
      )}
    </div>
  );
};

export default Heading2;
