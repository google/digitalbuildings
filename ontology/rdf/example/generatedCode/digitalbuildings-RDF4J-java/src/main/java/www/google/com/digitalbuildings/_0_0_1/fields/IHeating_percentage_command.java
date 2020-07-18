package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.ICommand;
import www.google.com.digitalbuildings._0_0_1.subfields.IHeating;
import www.google.com.digitalbuildings._0_0_1.subfields.IPercentage;

public interface IHeating_percentage_command extends IField{

	public IRI iri();

    public void addComposedOfCommand (ICommand parameter);

	public Set<ICommand> getComposedOfCommand();

    public void addComposedOfHeating (IHeating parameter);

	public Set<IHeating> getComposedOfHeating();

    public void addComposedOfPercentage (IPercentage parameter);

	public Set<IPercentage> getComposedOfPercentage();

}