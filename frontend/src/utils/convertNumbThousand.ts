const convertNumbThousand = (x?: number): string => {
  if (!x) {
    return "0";
  }
  return x.toLocaleString("vi-VN");
};
export default convertNumbThousand;
