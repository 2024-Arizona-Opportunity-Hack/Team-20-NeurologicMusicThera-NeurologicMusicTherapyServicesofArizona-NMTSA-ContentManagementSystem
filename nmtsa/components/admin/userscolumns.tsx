import { ColumnDef } from "@tanstack/react-table";

export type User = {
    id: number,
    username: string,
    email: string
};

export const userscolumns: Array<ColumnDef<User>> = [
    {
        header: "ID",
        accessorKey: "id",
    },
    {
        header: "Username",
        accessorKey: "username",
    },
    {
        header: "email",
        accessorKey: "email",
    },
];

