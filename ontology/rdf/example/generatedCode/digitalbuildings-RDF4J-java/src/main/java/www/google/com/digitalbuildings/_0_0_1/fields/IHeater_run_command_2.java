package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.ICommand;
import www.google.com.digitalbuildings._0_0_1.subfields.IHeater;
import www.google.com.digitalbuildings._0_0_1.subfields.IRun;

public interface IHeater_run_command_2 extends IField{

	public IRI iri();

    public void addComposedOfCommand (ICommand parameter);

	public Set<ICommand> getComposedOfCommand();

    public void addComposedOfHeater (IHeater parameter);

	public Set<IHeater> getComposedOfHeater();

    public void addComposedOfRun (IRun parameter);

	public Set<IRun> getComposedOfRun();

}