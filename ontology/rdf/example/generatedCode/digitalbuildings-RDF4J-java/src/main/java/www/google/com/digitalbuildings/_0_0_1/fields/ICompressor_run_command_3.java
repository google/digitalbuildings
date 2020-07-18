package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.ICommand;
import www.google.com.digitalbuildings._0_0_1.subfields.ICompressor;
import www.google.com.digitalbuildings._0_0_1.subfields.IRun;

public interface ICompressor_run_command_3 extends IField{

	public IRI iri();

    public void addComposedOfCommand (ICommand parameter);

	public Set<ICommand> getComposedOfCommand();

    public void addComposedOfCompressor (ICompressor parameter);

	public Set<ICompressor> getComposedOfCompressor();

    public void addComposedOfRun (IRun parameter);

	public Set<IRun> getComposedOfRun();

}