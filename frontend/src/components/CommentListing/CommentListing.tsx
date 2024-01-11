import { StarIcon } from "@heroicons/react/24/solid";
import React, { FC } from "react";
import Avatar from "shared/Avatar/Avatar";

interface CommentListingDataType {
  first_name: string;
  last_name: string;
  avatar?: string;
  // date: string;
  comment: string;
  rating: number;
}

export interface CommentListingProps {
  className?: string;
  data?: CommentListingDataType;
  // hasListingTitle?: boolean;
}

const DEMO_DATA: CommentListingDataType = {
  first_name: "jasmine",
  last_name: "josh",
  comment:
    "like it",
  rating: 5,
};

const CommentListing: FC<CommentListingProps> = ({
  className = "",
  data = DEMO_DATA,
  // hasListingTitle,
}) => {
  return (
    <div
      className={`nc-CommentListing flex space-x-4 ${className}`}
      data-nc-id="CommentListing"
    >
      <div className="pt-0.5">
        <Avatar
          sizeClass="h-10 w-10 text-lg"
          radius="rounded-full"
          userName={data.first_name}
          imgUrl={data.avatar}
        />
      </div>
      <div className="flex-grow">
        <div className="flex justify-between space-x-3">
          <div className="flex flex-col">
            <div className="text-sm font-semibold">
              <span>{data.first_name + " " + data.last_name}</span>
            </div>
          </div>
          <div className="flex text-yellow-500">
            <StarIcon className="w-4 h-4" />
            <StarIcon className="w-4 h-4" />
            <StarIcon className="w-4 h-4" />
            <StarIcon className="w-4 h-4" />
            <StarIcon className="w-4 h-4" />
          </div>
        </div>
        <span className="block mt-3 text-neutral-6000 dark:text-neutral-300">
          {data.comment}
        </span>
      </div>
    </div>
  );
};

export default CommentListing;
