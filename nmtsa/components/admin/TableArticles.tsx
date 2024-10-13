"use client"

import {
  ColumnDef,
  flexRender,
  getCoreRowModel,
  useReactTable,
  getPaginationRowModel,
  ColumnFiltersState,
  getFilteredRowModel
} from "@tanstack/react-table"

import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"

import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import React from "react"

interface DataTableProps<TData, TValue> {
  columns: ColumnDef<TData, TValue>[]
  data: TData[]
}

export function DataTableArticles<TData, TValue>({
  columns,
  data,
}: DataTableProps<TData, TValue>) {
  const [columnFilters, setColumnFilters] = React.useState<ColumnFiltersState>(
    []
  )
  const table = useReactTable({
    data,
    columns,
    getCoreRowModel: getCoreRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
    onColumnFiltersChange: setColumnFilters,
    getFilteredRowModel: getFilteredRowModel(),
    state: {
        columnFilters,
      },
  })

  return (
    <div>
        <div className="flex space-x-10">
        <div className="flex items-center py-4">
        <Input
          placeholder="Filter titles..."
          value={(table.getColumn("title")?.getFilterValue() as string) ?? ""}
          onChange={(event) =>
            table.getColumn("title")?.setFilterValue(event.target.value)
          }
          className="max-w-sm"
        />
      </div>
      <div className="flex items-center py-4">
    <Input
      placeholder="Filter categories..."
      value={(table.getColumn("category")?.getFilterValue() as string) ?? ""}
      onChange={(event) =>
        table.getColumn("category")?.setFilterValue(event.target.value)
      }
      className="max-w-sm mx-auto"
    />
  </div>
  <div className="flex items-center py-4">
    <Input
      placeholder="Filter tags..."
      value={(table.getColumn("tags")?.getFilterValue() as string) ?? ""}
      onChange={(event) =>
        table.getColumn("tags")?.setFilterValue(event.target.value)
      }
      className="max-w-sm mx-auto"
    />
  </div>
  <div className="flex items-center py-4">
    <Input
      placeholder="Filter by date..."
      value={(table.getColumn("date")?.getFilterValue() as string) ?? ""}
      onChange={(event) =>
        table.getColumn("date")?.setFilterValue(event.target.value)
      }
      className="max-w-sm mx-auto"
    />
  </div>
  <div className="flex items-center py-4">
    <Input
      placeholder="Filter files..."
      value={(table.getColumn("file")?.getFilterValue() as string) ?? ""}
      onChange={(event) =>
        table.getColumn("file")?.setFilterValue(event.target.value)
      }
      className="max-w-sm mx-auto"
    />
  </div>
  <div className="flex items-center py-4">
    <Input
      placeholder="Filter by access..."
      value={(table.getColumn("access")?.getFilterValue() as string) ?? ""}
      onChange={(event) =>
        table.getColumn("access")?.setFilterValue(event.target.value)
      }
      className="max-w-sm mx-auto"
    />
  </div>
  </div>
    <div className="rounded-md border shadow-sm bg-white">
      <Table>
        <TableHeader>
          {table.getHeaderGroups().map((headerGroup) => (
            <TableRow key={headerGroup.id}>
              {headerGroup.headers.map((header) => {
                return (
                  <TableHead key={header.id}>
                    {header.isPlaceholder
                      ? null
                      : flexRender(
                          header.column.columnDef.header,
                          header.getContext()
                        )}
                  </TableHead>
                )
              })}
            </TableRow>
          ))}
        </TableHeader>
        <TableBody>
          {table.getRowModel().rows?.length ? (
            table.getRowModel().rows.map((row) => (
              <TableRow
                key={row.id}
                data-state={row.getIsSelected() && "selected"}
              >
                {row.getVisibleCells().map((cell) => (
                  <TableCell key={cell.id}>
                    {flexRender(cell.column.columnDef.cell, cell.getContext())}
                  </TableCell>
                ))}
              </TableRow>
            ))
          ) : (
            <TableRow>
              <TableCell colSpan={columns.length} className="h-24 text-center">
                No results.
              </TableCell>
            </TableRow>
          )}
        </TableBody>
      </Table>
    </div>
    <div className="flex items-center justify-end space-x-2 py-4">
        <Button
          variant="outline"
          size="sm"
          onClick={() => table.previousPage()}
          disabled={!table.getCanPreviousPage()}
        >
          Previous
        </Button>
        <Button
          variant="outline"
          size="sm"
          onClick={() => table.nextPage()}
          disabled={!table.getCanNextPage()}
        >
          Next
        </Button>
      </div>
    </div>
  )
}