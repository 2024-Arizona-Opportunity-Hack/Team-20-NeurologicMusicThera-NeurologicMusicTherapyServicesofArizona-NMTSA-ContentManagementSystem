import {
    Table,
    TableBody,
    TableCaption,
    TableCell,
    TableFooter,
    TableHead,
    TableHeader,
    TableRow,
  } from "@/components/ui/table"
  
  interface TableVideosProps {
    name: string,
    list: Array<{
      title: string,
      filePath: string,
      transcript: string,
      group: string,
      category: string,
      tags: Array<string>
    }>
  }
  
  export function TableVideos(props: TableVideosProps) {
    return (
      <Table>
        <TableCaption>Manage your videos.</TableCaption>
        <TableHeader>
          <TableRow>
            <TableHead>Title</TableHead>
            <TableHead>File Path</TableHead>
            <TableHead>Transcript</TableHead>
            <TableHead>Group</TableHead>
            <TableHead>Category</TableHead>
            <TableHead>Tags</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {props.list.map((row) => (
            <TableRow key={row.title}>
              <TableCell>{row.title}</TableCell>
              <TableCell>{row.filePath}</TableCell>
              <TableCell>{row.transcript}</TableCell>
              <TableCell>{row.group}</TableCell>
              <TableCell>{row.category}</TableCell>
              <TableCell>
                {
                  row.tags.map((tag, index) => (
                    <span key={tag}>
                      {tag}
                      {index < row.tags.length - 1 ? ", " : ""}
                    </span>
                  ))
                }
                </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    )
  }
  