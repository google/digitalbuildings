package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.ICommand;
import www.google.com.digitalbuildings._0_0_1.subfields.IPercentage;
import www.google.com.digitalbuildings._0_0_1.subfields.ITilt;
import www.google.com.digitalbuildings._0_0_1.subfields.IShade;

public interface IShade_tilt_percentage_command extends IField{

	public IRI iri();

    public void addComposedOfCommand (ICommand parameter);

	public Set<ICommand> getComposedOfCommand();

    public void addComposedOfPercentage (IPercentage parameter);

	public Set<IPercentage> getComposedOfPercentage();

    public void addComposedOfShade (IShade parameter);

	public Set<IShade> getComposedOfShade();

    public void addComposedOfTilt (ITilt parameter);

	public Set<ITilt> getComposedOfTilt();

}