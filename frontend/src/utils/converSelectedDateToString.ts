import { DateRage } from "components/HeroSearchForm/type";

const converSelectedDateToString = ([startDate, endDate]: DateRage) => {
  const dateString =
    (startDate?.toLocaleDateString("vi-VN", {
      month: "short",
      day: "2-digit",
    }) || "") +
    (endDate
      ? " - " +
        endDate?.toLocaleDateString("vi-VN", {
          month: "short",
          day: "2-digit",
        })
      : "");
  return dateString;
};

export default converSelectedDateToString;
